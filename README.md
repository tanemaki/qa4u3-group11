# QA4U3 Group11

[QA4U3](https://altema.is.tohoku.ac.jp/QA4U3/)のGroup11の活動のために作成されたリポジトリです。

## 使用ツール

- プロジェクト作成＆Pythonパッケージマネージャー [uv](https://docs.astral.sh/uv/)
- コード整形など [Ruff](https://docs.astral.sh/ruff/)

## はじめての使い方

1. [Docker Desktop](https://www.docker.com/ja-jp/products/docker-desktop/)をインストールし、起動します。
1. [仮のデータセット](https://drive.google.com/drive/folders/1SemmXN9oCed0N0fkdnYHC0rVgbMH6KLE)をダウンロードし、解凍しておきます。
1. このリポジトリをクローンします。
1. VS Codeを開きます。
1. `.devcontainer/.env.example`というファイルをコピーして、`.devcontainer/.env`というファイルを作成します（注意：このファイルにはユーザーの環境依存な情報を書き込むことになるのでgitでコミットしないで下さい。デフォルトでgitのトラッキングから外しているので特に何もしなくて大丈夫です）。
1. `.devcontainer/.env`の`LOCAL_DATASETS_PATH`をデータセットが保存されているディレクトリに変更します。例えば、先ほどダウンロードしたデータセットが`/path/to/your/local/datasets`に保存されている場合、以下のように書き換えます。

    ```bash
    LOCAL_DATASETS_PATH=/path/to/your/local/datasets
    ```

1. [Dev ContainersというVS Codeの拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)をインストールします。
1. 左下の「><」をクリックして、コマンドパレットを開きます。
1. `Remote-Containers: Reopen in Container`を選択します。
1. コンテナの起動と同時に新しいウィンドウが開き、画面左下に「開発コンテナ: python @ desktop-linux」と表示されているのを確認します。
1. ターミナルを開いて、`(workspace) root@9dd39b93510f:/workspace#`のように表示されていることを確認します。
1. `python --version`を実行してPythonのバージョンが`Python 3.12.8`と表示されることを確認します。
1. `streamlit run app/app.py`を実行して、アプリが起動したら成功です。やったね！

## その他の使い方

### Pythonパッケージのインストール

```bash
uv add <package-name>
```

### Pythonパッケージのアンインストール

```bash
uv remove <package-name>
```

## このリポジトリをどのように作成したか

1. `qa4u3-group11`という名前でプロジェクトを作成

    ```bash
    uv init qa4u3-group11  # 今回はアプリ形式（flat layout）を採用
    # uv init qa4u3-group11 --lib # ライブラリ形式（src layout）にしたければこちら

    # プロジェクトディレクトリの中に移動
    cd qa4u3-group11
    ```

2. `.devcontainer`の中身を他のリポジトリからコピーしてきて使いやすいように変更

3. `app/app.py`を作成してDONE!
