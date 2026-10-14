import os
import jwt

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        # Routes accessibles sans connexion
        public_paths = {
            "/",
            "/login",
            "/health",
            "/docs",
            "/openapi.json",
            "/redoc",
            "/favicon.ico",
            "/api/v1/users/register",
            "/api/v1/users/login",
        }

        path = request.url.path

        if (
            path in public_paths
            or path.startswith("/frontend/")
        ):
            return await call_next(request)

        authorization = request.headers.get("Authorization")

        if not authorization:
            return JSONResponse(
                status_code=401,
                content={"detail": "Token manquant"}
            )

        scheme, separator, token = authorization.partition(" ")

        if not separator or scheme.lower() != "bearer" or not token:
            return JSONResponse(
                status_code=401,
                content={"detail": "Format du token invalide"}
            )

        try:
            payload = jwt.decode(
                token,
                os.environ["JWT_SECRET"],
                algorithms=["HS256"]
            )

            user_id = payload.get("sub")

            if not isinstance(user_id, str) or not user_id:
                raise jwt.InvalidTokenError()

            request.state.user_id = user_id

        except jwt.InvalidTokenError:
            return JSONResponse(
                status_code=401,
                content={"detail": "Token invalide ou expiré"}
            )

        return await call_next(request)