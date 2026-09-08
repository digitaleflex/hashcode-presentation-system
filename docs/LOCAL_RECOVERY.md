# Local Recovery and Dependency Policy

## If your local workspace is broken after npm audit fix --force

Do not run another forced audit fix.

Use:

```powershell
git status
git fetch origin
git pull origin main
npm install
npm run
npm run check
```

If package files were locally modified and you intentionally want to discard those changes:

```powershell
git restore package.json package-lock.json
git pull origin main
npm install
npm run check
```

Only restore `package-lock.json` if it exists in your local checkout.

## Supported commands

- `npm run generate`
- `npm run check`
- `npm run dev`
- `npm run dev:showcase`
- `npm run build`
- `npm run build:showcase`
- `npm run export`
- `npm run export:all`

## Security policy

Do not use `npm audit fix --force` as a routine maintenance command. Major dependency upgrades must be tested through CI because Slidev upgrades can change rendering and export behavior.
