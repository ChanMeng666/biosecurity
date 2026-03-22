import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "cdn.pixabay.com" },
      { protocol: "https", hostname: "pixabay.com" },
    ],
  },
};

export default nextConfig;
