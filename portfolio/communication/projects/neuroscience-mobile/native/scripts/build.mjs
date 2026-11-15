// Copies the phone tour from website/neuroscience-mobile into dist/, with the shared
// website assets beside it, so the Android and iOS apps show exactly what the website shows.
import { cpSync, mkdirSync, readFileSync, writeFileSync, rmSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const native = resolve(here, "..");
const website = resolve(native, "../../../../website");
const output = resolve(native, "dist");
rmSync(output, { recursive: true, force: true });
mkdirSync(output, { recursive: true });
cpSync(resolve(website, "assets"), resolve(output, "assets"), { recursive: true });
mkdirSync(resolve(output, "img"), { recursive: true });
cpSync(resolve(website, "img/next-step-energy.jpg"), resolve(output, "img/next-step-energy.jpg"));
const html = readFileSync(resolve(website, "neuroscience-mobile/index.html"), "utf8")
  .replaceAll('"../assets/', '"assets/').replaceAll('"../img/', '"img/').replaceAll('href="../index.html"', 'href="index.html"')
  // The app is already installed, so drop the "get the Android app" line.
  .replace(/<p class="landing-try-note"><a href="download.html">[\s\S]*?<\/p>/, "");
writeFileSync(resolve(output, "index.html"), html);
cpSync(resolve(website, "neuroscience-mobile/manifest.webmanifest"), resolve(output, "manifest.webmanifest"));
console.log(`Copied the phone tour and shared assets into ${output}`);
