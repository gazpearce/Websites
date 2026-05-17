const STATIC_DIR = ".";

const MIME_TYPES: Record<string, string> = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".gif": "image/gif",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
  ".xml": "application/xml",
  ".txt": "text/plain; charset=utf-8",
  ".woff": "font/woff",
  ".woff2": "font/woff2",
  ".ttf": "font/ttf",
  ".eot": "application/vnd.ms-fontobject",
  ".otf": "font/otf",
  ".map": "application/json; charset=utf-8",
};

function getContentType(path: string): string {
  const ext = "." + path.split(".").pop()?.toLowerCase();
  return MIME_TYPES[ext] || "application/octet-stream";
}

async function serveStatic(req: Request): Promise<Response> {
  const url = new URL(req.url);
  let pathname = url.pathname;

  // Remove trailing slash for consistency
  if (pathname !== "/" && pathname.endsWith("/")) {
    pathname = pathname.slice(0, -1);
  }

  // Default to index.html for root or directories
  if (pathname === "/" || !pathname.includes(".")) {
    pathname = pathname === "/" ? "/index.html" : pathname + "/index.html";
  }

  const filePath = STATIC_DIR + pathname;

  try {
    const file = await Deno.stat(filePath);
    if (file.isFile) {
      const content = await Deno.readFile(filePath);
      const contentType = getContentType(pathname);
      return new Response(content, {
        headers: {
          "Content-Type": contentType,
          "Cache-Control": "public, max-age=3600",
        },
      });
    }
  } catch {
    // File not found, try 404.html
  }

  // Try 404.html
  try {
    const notFound = await Deno.readFile(STATIC_DIR + "/404.html");
    return new Response(notFound, {
      status: 404,
      headers: {
        "Content-Type": "text/html; charset=utf-8",
      },
    });
  } catch {
    return new Response("Not Found", { status: 404 });
  }
}

Deno.serve(serveStatic);
