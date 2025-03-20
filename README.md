# QA4U3 Group11

[QA4U3](https://altema.is.tohoku.ac.jp/QA4U3/)のGroup11の活動のために作成されたリポジトリです。

## 使用ツール

- プロジェクト作成＆Pythonパッケージマネージャー [uv](https://docs.astral.sh/uv/)
- コード整形など [Ruff](https://docs.astral.sh/ruff/)

## はじめての使い方

1. このリポジトリをクローンします。
2. VS Codeを開きます。
3. [Dev ContainersというVS Codeの拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)をインストールします。
4. 左下の「><」をクリックして、コマンドパレットを開きます。
5. `Remote-Containers: Reopen in Container`を選択します。
6. コンテナの起動と同時に新しいウィンドウが開き、画面左下に「開発コンテナ: python @ desktop-linux」と表示されているのを確認します。
7. ターミナルを開いて、`(workspace) root@9dd39b93510f:/workspace#`のように表示されていることを確認します。
8. `python --version`を実行してPythonのバージョンが`Python 3.12.8`と表示されることを確認します。
9. `streamlit run app/app.py`を実行して、アプリが起動したら成功です。やったね！

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
