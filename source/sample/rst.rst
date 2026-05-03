restructuredtextの書き方メモ
#############################

テキスト装飾
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            通常
      - 通常
    * - .. code:: rst

            *斜体*
      - *斜体*
    * - .. code:: rst 

            **太字**
      - **太字**
    * - .. code:: rst

            ``インラインリテラル``
      - ``インラインリテラル``
    * - .. code:: rst

            :sub:`下付き文字`
      - 通常 :sub:`下付き文字`
    * - .. code:: rst

            :sup:`上付き文字`
      - 通常 :sup:`上付き文字`
    * - .. code:: rst

            :abbr:`略語 (略語の説明文)`
      - :abbr:`略語 (略語の説明文)`
    * - .. code:: rst

            :file:`/path/to/file/`

            :file:`/path/to/installed/v.{x}.{y}/bin/`
      - :file:`/path/to/file/`

        :file:`/path/to/installed/v.{x}.{y}/bin/`
    * - .. code:: rst

            :program:`mytool`
      - :program:`mytool`
    * - .. code:: rst

            :kbd:`Ctrl` + :kbd:`C`
      - :kbd:`Ctrl` + :kbd:`C`
    * - .. code:: rst

            :menuselection:`Start --> Programs`
      - :menuselection:`Start --> Programs`
    * - .. code:: rst

            :cve:`2020-10735`
      - :cve:`2020-10735`
    * - .. code:: rst

            :cwe:`787`
      - :cwe:`787`
    * - .. code:: rst

            :rfc:`7231`
      - :rfc:`7231`


引用
=============================

ソース
    .. code:: rst

        通常

            引用文


出力
    通常

        引用文


定型書式
=============================

コマンドライン引数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            ``mytool`` のオプション

            .. program:: mytool

            .. option:: -output <path>

                出力先ディレクトリ(コマンドライン引数の定型文)

            ``yourtool`` のオプション

            .. program:: yourtool

            .. option:: -output

                出力方法

            .. option:: --input

                入力方法
      - ``mytool`` のオプション

        .. program:: mytool

        .. option:: --output <path>

            出力先ディレクトリ(コマンドライン引数の定型文)

        ``yourtool`` のオプション

        .. program:: yourtool

        .. option:: --output

            出力方法

        .. option:: --input

            入力方法


.. hint:: programディレクティブを使用するとoptionラベルで参照するときに同じオプション名も区別して相互参照できる。

環境変数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            .. envvar:: MYTOOL_INSTALLED_PATH

                インストールされたディレクトリパス(環境変数の定型文)
      - .. envvar:: MYTOOL_INSTALLED_PATH

            インストールされたディレクトリパス(環境変数の定型文)


設定ファイル
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            .. confval:: log-path
                :type: ``string``
                :default: "/var/log/my/tool.log"

                ログの格納場所を指定する。(コンフィグ項目の定型文)
      - .. confval:: log-path
            :type: ``string``
            :default: "/var/log/my/tool.log"

            ログの格納場所を指定する。(コンフィグ項目の定型文)

箇条書き
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            - 箇条書き項目1
            - 箇条書き項目2
            - 箇条書き項目3(サブ項目は空行を入れる)

              - サブ項目1(インデントは引用ブロックより小さくする)
              - サブ項目2
            
                - サブサブ項目1 
                - サブサブ項目2 
                - サブサブ項目3
            
              - サブ項目3(サブ項目を終了する場合は空行を入れる)

            - 箇条書き項目4
            - 箇条書き項目5
      - - 箇条書き項目1
        - 箇条書き項目2
        - 箇条書き項目3(サブ項目は空行を入れる)

          - サブ項目1(サブ項目のインデントは引用ブロックのスペース数より少なくする)
          - サブ項目2
        
            - サブサブ項目1 
            - サブサブ項目2 
            - サブサブ項目3
        
          - サブ項目3(サブ項目を終了する場合は空行を入れる)

        - 箇条書き項目4
        - 箇条書き項目5


番号付き箇条書き
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            #. 番号付きリスト
            #. 番号付きリスト
            #. 番号付きリスト
            #. 番号付きリスト

            a. 番号付きリスト
            #. 番号付きリスト
            #. 番号付きリスト
            #. 番号付きリスト

            A. 番号付きリスト
            #. 番号付きリスト
            #. 番号付きリスト
            #. 番号付きリスト

            i. 番号付きリスト
            #. 番号付きリスト
            #. 番号付きリスト
            #. 番号付きリスト
      - #. 番号付きリスト
        #. 番号付きリスト
        #. 番号付きリスト
        #. 番号付きリスト

        a. 番号付きリスト
        #. 番号付きリスト
        #. 番号付きリスト
        #. 番号付きリスト

        A. 番号付きリスト
        #. 番号付きリスト
        #. 番号付きリスト
        #. 番号付きリスト

        i. 番号付きリスト
        #. 番号付きリスト
        #. 番号付きリスト
        #. 番号付きリスト



定義リスト
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            :定義1: 定義1の説明
            :定義2: 定義2の説明
      - :定義1: 定義1の説明
        :定義2: 定義2の説明
    * - .. code:: rst

            定義1
                定義1の説明

            定義2
                定義2の説明
      - 定義1
            定義1の説明

        定義2
            定義2の説明


.. note:: 定義と説明の間には空行を入れない。空行を入れると引用になる。


用語集
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1

    * - **ソース**
      - **出力**
    * - .. code:: rst

            .. glossary::
                :sorted:

                用語1
                    用語1の説明文

                用語4 : t4
                用語5 : t5
                    用語4と用語5の説明文（指定すればソートされる）

                用語2
                用語3
                    用語2と用語3の説明文（まとめられる）
      - .. glossary::
            :sorted:

            用語1
                用語1の説明文

            用語4 : t4
            用語5 : t5
                用語4と用語5の説明文（指定すればソートされる）

            用語2
            用語3
                用語2と用語3の説明文（まとめられる）

注釈
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%
    :class: longtable

    * - **ソース**
      - **出力**
    * - .. code:: rst

            .. note:: note

      - .. note:: note

    * - .. code:: rst

            .. attention:: attention

      - .. attention:: attention

    * - .. code:: rst

            .. caution:: caution

      - .. caution:: caution

    * - .. code:: rst

            .. warning:: warning

      - .. warning:: warning

    * - .. code:: rst

            .. danger:: danger

      - .. danger:: danger

    * - .. code:: rst

            .. error:: error

      - .. error:: error

    * - .. code:: rst

            .. hint:: hint

      - .. hint:: hint

    * - .. code:: rst

            .. tip:: tip

      - .. tip:: tip

    * - .. code:: rst

            .. important:: important

      - .. important:: important

    * - .. code:: rst

            .. seealso:: seealso

      - .. seealso:: seealso

    * - .. code:: rst

            .. admonition:: カスタムタイトル
                :class: note

                classを指定することで注釈タイプを指定できる。

      - .. admonition:: カスタムタイトル
            :class: note

            classを指定することで注釈タイプを指定できる。


ハイパーリンク
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            URLを直接書く https://github.com/toald11/test-sphinx
      - URLを直接書く https://github.com/toald11/test-sphinx
    * - .. code:: rst

            `表示文字 <https://github.com/toald11/test-sphinx>`_
      - `表示文字 <https://github.com/toald11/test-sphinx>`_
    * - .. code:: rst

            :doc:`pdf`

            :doc:`表示文字 <pdf>`
      - :doc:`pdf`

        :doc:`表示文字 <pdf>`


脚注
=============================

ソース
    .. code:: rst
        
        ツールA [#f1]_ は、ツールB [#f2]_ と互換性がある。

        .. [#f1] 脚注1の説明文を書く。脚注1の説明文を書く。脚注1の説明文を書く。
        .. [#f2] 脚注2の説明文を書く。脚注2の説明文を書く。脚注2の説明文を書く。

出力
    ツールA [#f1]_ は、ツールB [#f2]_ と互換性がある。

    .. [#f1] 脚注1の説明文を書く。脚注1の説明文を書く。脚注1の説明文を書く。
    .. [#f2] 脚注2の説明文を書く。脚注2の説明文を書く。脚注2の説明文を書く。


.. _sec_reference:
相互参照
=============================

リスト、図、表への参照
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            :numref:`list-example-codeblock`

            :numref:`fig-example-al-center`

            :numref:`fig-example-dark`

            :numref:`fig-example-light`

            :numref:`uml-example-inline`

            :numref:`tab-example-simple`

            :numref:`tab-example-csv-table`

            :numref:`tab-example-list-table`
      - :numref:`list-example-codeblock`

        :numref:`fig-example-al-center`

        :numref:`fig-example-dark`

        :numref:`fig-example-light`

        :numref:`uml-example-inline`

        :numref:`tab-example-simple`

        :numref:`tab-example-csv-table`

        :numref:`tab-example-list-table`


章、ラベルへの参照
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            .. _sec_reference:
            相互参照
            =============================

            参照に関する表現方法を :ref:`sec_reference` で説明する。

      - 参照に関する表現方法を :ref:`sec_reference` で説明する。


定型書式への参照
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst 

            :option:`mytool --output`

            :option:`yourtool --output`

            :option:`yourtool --input`

            :envvar:`MYTOOL_INSTALLED_PATH`

            :confval:`log-path`
      - :option:`mytool --output`

        :option:`yourtool --output`

        :option:`yourtool --input`

        :envvar:`MYTOOL_INSTALLED_PATH`

        :confval:`log-path`


用語集への参照
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            :term:`用語1`

            :term:`用語2`

            :term:`用語3`

            :term:`用語4`

            :term:`用語5`
      - :term:`用語1`

        :term:`用語2`

        :term:`用語3`

        :term:`用語4`

        :term:`用語5`


数式への参照
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            数式 :eq:`math-sample` を参照
      - 数式 :eq:`math-sample` を参照


目次
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            .. toctree::
                :maxdepth: 2
                :name: toc-top
                :numbered:
                :glob:
                :caption: 目次:

                sample/rst
                sample/theme
                sample/pdf
      - 目次の出力例は :doc:`/index` を参照

.. confval:: glob

    目次に正規表現を使用

.. confval:: numbered

    目次に章番号を自動付与

置換
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            .. |target| replace:: NetworkModule

            このドキュメントは |target| に適用される。
      - .. |target| replace:: NetworkModule

        このドキュメントは |target| に適用される。
    * - .. code:: rst

            releaseは |release|

            versionは |version|

            todayは |today|

            translation progressは |translation progress|
      - releaseは |release|

        versionは |version|

        todayは |today|

        translation progressは |translation progress|


コメント
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            .. これはコメントです。

            ..
                複数行のコメントも
                書けます。
      - .. これはコメントです。

        ..
            複数行のコメントも
            書けます。

コードブロック
=============================

ソース
    .. code:: rst

        .. code:: bash

            cd test-sphinx
            python -m uv run sphinx-build -M latexpdfja source/ build/
            echo "Done!"


        .. code-block:: bash
            :name: list-example-codeblock
            :caption: code-blockのタイトル
            :linenos:

            cd test-sphinx
            python -m uv run sphinx-build -M latexpdfja source/ build/
            echo "Done!"

出力
    .. code:: bash

        cd test-sphinx
        python -m uv run sphinx-build -M latexpdfja source/ build/
        echo "Done!"


    .. code-block:: bash
        :name: list-example-codeblock
        :caption: code-blockのタイトル
        :linenos:

        cd test-sphinx
        python -m uv run sphinx-build -M latexpdfja source/ build/
        echo "Done!"



画像
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            .. figure:: https://avatars.githubusercontent.com/u/40462478
                :name: fig-example-al-center
                :align: center
                
                画像の貼り付け
      - .. figure:: https://avatars.githubusercontent.com/u/40462478
            :name: fig-example-al-center
            
            画像の貼り付け
    * - .. code:: rst

            .. figure:: ../_static/icon_dark.png
                :name: fig-example-dark
                :figclass: only-dark
                
                ダークテーマの画像

            .. figure:: ../_static/icon_light.png
                :name: fig-example-light
                :figclass: only-light
                
                ライトテーマの画像
      - .. figure:: ../_static/icon_dark.png
            :name: fig-example-dark
            :figclass: only-dark
            
            ダークテーマの画像

        .. figure:: ../_static/icon_light.png
            :name: fig-example-light
            :figclass: only-light
            
            ライトテーマの画像

.. warning:: 
    
    figclassによるダーク/ライトテーマの切り替えは、以下のケースでは有用ではありません。

    :PDFの出力: 両方の図が出力される。
    :numfigとの併用: 図の参照番号は共有されない。


PlantUML
=============================

設定
    設定例を以下に示す。
    特に日本語フォントを使用することに特化した例である。

    .. code-block:: bash
        :name: list-uml-install
        :caption: plantumlのインストール

        wget openjdk-17-jre-headless fonts-noto-cjk
        wget -O /usr/local/bin/plantuml.jar https://github.com/plantuml/plantuml/releases/download/v1.2026.2/plantuml-mit-1.2026.2.jar

    .. code-block:: python
        :name: list-uml-confpy
        :caption: conf.pyの設定例(日本語設定)

        extensions.append("sphinxcontrib.plantuml")
        plantuml = 'java -jar /usr/local/bin/plantuml.jar -config /usr/local/share/jp.pu'

    .. code-block::
        :name: list-uml-jppu
        :caption: /usr/local/share/jp.pu の設定例(日本語フォントをデフォルト使用する)

        skinparam defaultFontName "Noto Sans CJK JP"
        skinparam dpi 100

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            .. uml:: 
                :name: uml-example-inline
                :scale: 100 %
                :caption: PlantUMLの出力例

                "A" -> "B" : 日本語の表示には
                "A" -> "B" : フォントのインストールと
                "A" -> "B" : デフォルトフォントの指定が便利
      - .. uml:: 
            :name: uml-example-inline
            :scale: 100 %
            :caption: PlantUMLの出力例

            "A" -> "B" : 日本語の表示には
            "A" -> "B" : フォントのインストールと
            "A" -> "B" : デフォルトフォントの指定が便利


表
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            .. table:: シンプルテーブル
                :name: tab-example-simple
                :widths: 10,70,20

                ======== ======== ========
                header 1 header 2 header 3
                ======== ======== ========
                1        2        3
                4        5        6
                7        8        9
                ======== ======== ========
      - .. table:: シンプルテーブル
            :name: tab-example-simple
            :widths: 10,70,20

            ======== ======== ========
            header 1 header 2 header 3
            ======== ======== ========
            1        2        3
            4        5        6
            7        8        9
            ======== ======== ========
    * - .. code:: rst

            .. csv-table:: CSVテーブル
                :name: tab-example-csv-table
                :header-rows: 1
                :stub-columns: 1
                :widths: 10,70,20

                header 1,header 2,header 3
                1,2,3
                4,5,6
                7,8,9
      - .. csv-table:: CSVテーブル
            :name: tab-example-csv-table
            :header-rows: 1
            :stub-columns: 1
            :widths: 10,70,20

            header 1,header 2,header 3
            1,2,3
            4,5,6
            7,8,9
    * - .. code:: rst

            .. list-table:: リストテーブル
                :name: tab-example-list-table
                :header-rows: 1
                :stub-columns: 1
                :widths: 10,70,20

                * - header 1
                - header 2
                - header 3
                * - 1
                - 2
                - 3
                * - 4
                - 5
                - 6
                * - 7
                - 8
                - 9
      - .. list-table:: リストテーブル
            :name: tab-example-list-table
            :header-rows: 1
            :stub-columns: 1
            :widths: 10,70,20

            * - header 1
              - header 2
              - header 3
            * - 1
              - 2
              - 3
            * - 4
              - 5
              - 6
            * - 7
              - 8
              - 9


数式
=============================

.. list-table::
    :header-rows: 1
    :widths: 1 1
    :width: 100%

    * - **ソース**
      - **出力**
    * - .. code:: rst

            インライン数式 :math:`f = ma^2` は文書中に表示できる
      - インライン数式 :math:`f = ma^2` は文書中に表示できる
    * - .. code:: rst

            .. math::
                :label: math-sample

                (a + b)^2 &= a^2 + 2ab + b^2 \\
                (a - b)^2 &= a^2 - 2ab + b^2

            .. math::
                :label: math-sample2

                (a + b)(a - b) &= a^2 - b^2 \\
      - .. math::
            :label: math-sample

            (a + b)^2 = a^2 + 2ab + b^2 \\
            (a - b)^2 = a^2 - 2ab + b^2

        .. math::
            :label: math-sample2

            (a + b)(a - b) = a^2 - b^2 \\


.. warning:: 表の中に数式を入れる場合、等式で整列する ``&=`` を使用するとLaTeX PDFを出力する際にエラーになる。


バージョン表記
=============================

ソース
    .. code:: rst

        .. version-added:: v1.2.2 :option:`yourtool --input` を追加
        .. version-changed:: v1.2.2 :option:`mytool --output` の処理を変更
        .. version-deprecated:: v1.2.2 `mytool -o` は、 `mytool --output` に置き換わりました。
        .. version-added:: v1.2.1 :option:`yourtool --output` を追加
        .. version-removed:: v1.2.1 :option:`yourtool --verbose` を削除

出力
    .. version-added:: v1.2.2 :option:`yourtool --input` を追加
    .. version-changed:: v1.2.2 :option:`mytool --output` の処理を変更
    .. version-deprecated:: v1.2.2 `mytool -o` は、 `mytool --output` に置き換わりました。
    .. version-added:: v1.2.1 :option:`yourtool --output` を追加
    .. version-removed:: v1.2.1 :option:`yourtool --verbose` を削除

