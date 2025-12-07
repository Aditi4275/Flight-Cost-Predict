# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set the working directory to /app
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy the lockfile and pyproject.toml
COPY uv.lock pyproject.toml /app/

# Install the project's dependencies using the lockfile and settings
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the project source code
COPY . /app/

# Install the project itself
RUN uv sync --frozen --no-dev

# Place the virtual environment in the PATH
ENV PATH="/app/.venv/bin:/home/ranit/.local/share/mise/installs/go/1.25.3/bin:/home/ranit/.local/share/mise/installs/node/24.11.1/bin:/home/ranit/.local/share/mise/installs/python/3.14.0/bin:/home/ranit/.local/share/omarchy/bin/:/home/ranit/.local/share/../bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl"

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
