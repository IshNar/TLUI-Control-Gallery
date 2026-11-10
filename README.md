# TLUI Control Gallery

A community catalog of reusable, declarative TL_UI controls. SDK and Designer implementation sources are not included.

## Use

Use TL_UI Designer 0.10.75 or newer: **Design → 공유 컨트롤 갤러리**. Refresh the catalog, download/preview, then install to the toolbox. Alternatively download a `.tluicontrol` file and choose **파일 가져오기**. Installed definitions work offline. Versions have independent type keys; existing canvases keep their selected version. The shared TL_UI runtime is required; these packages do not carry a new DLL.

## Share

Select your custom control in Designer and export from the gallery dialog. Supply a lowercase package ID, `major.minor.patch` version, author and license. Fork this repository and add `packages/<id>/<version>.tluicontrol`, then submit a pull request. Do not include company projects, credentials, SDK binaries or device data. Contributors must have redistribution rights.

Run `python scripts/build_catalog.py` before submission. Existing published versions must not be edited; publish a new version. Maintainers review contributions before merging. The workflow validates packages, rebuilds the catalog, and deploys GitHub Pages. Pull requests do not receive deployment permissions.

This first format supports declarative custom-runtime-v1 controls only. It does not execute uploaded C++, scripts, native plugins or DLLs. A future native-pack format requires a separate trust/build/distribution design.

## Local preview

Run `python -m http.server 8080` here and open localhost:8080. No database or npm build is required. Public catalog: https://ishnar.github.io/TLUI-Control-Gallery/
