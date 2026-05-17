HTMLのカスタマイズ
===================

HTMLの出力に関する設定は、 conf.py への設定を基本とする。
conf.py では、テーマ固有の設定やCSSファイルの追加などによって見た目を設定できる。

このドキュメントのHTMLテーマには Furo theme を使用する。
本章の説明も Furo theme を使用する前提で説明する。
Furo theme に固有の設定は本文中で注釈する。

`Furo themeの公式 <https://pradyunsg.me/furo/>`_


HTML出力に関する標準的な設定
-----------------------------

conf.py の設定値のうち、主要なものを `公式ドキュメント <https://www.sphinx-doc.org/ja/master/usage/configuration.html#options-for-html-output>`_ から抜粋する。



.. confval:: html_static_path
    :type: ``list[str]``
    :default: ``[]``

    静的ファイルを格納するディレクトリパスのリスト。
    このディレクトリにCSSファイル、JSファイル、画像ファイルなどを格納することで、HTMLテーマやLaTeXのスタイルで使用できるリソースをSphinxに明示できる。

.. confval:: templates_path
    :type: ``list[str]``
    :default: ``[]``

    テンプレートを格納するディレクトリパスのリスト。
    テンプレートは、標準またはテーマごとに用意されており、同名のファイルを配置することで上書きできる。
    また、独自のテンプレートを定義し配置することができる。

.. confval:: html_css_files
    :type: ``list[str | tuple[str, dict[str,str]]]``
    :default: ``[]``

    各HTMLが使用するCSSファイルのリスト。
    :confval:`templates_path` からの相対パスで指定する。
    もしくは、CSSのフルスキームURLを指定できる。

.. confval:: html_js_files
    :type: ``list[str | tuple[str, dict[str,str]]]``
    :default: ``[]``

    各HTMLが使用するJavascriptファイルのリスト。
    :confval:`templates_path` からの相対パスで指定する。
    もしくは、CSSのフルスキームURLを指定できる。

.. confval:: html_extra_path
    :type: ``list[str]``
    :default: ``[]``

    ドキュメントと直接関係のない追加ファイルのリスト。
    :file:`robots.txt` や :file:`.htaccess` の配置などに使用できる。

.. confval:: html_sidebars
    :type: ``dict[str, list[str]]``
    :default: `{}`

    ページごとのサイドバーテンプレートを定義する辞書オブジェクト。
    キーには、サイドバーを定義するページのパスを設定する。
    キーに ``**`` を指定すると、すべてのページのサイドバーに適用される。
    値は、ビルドインテンプレート、テーマが用意しているテンプレート、 :confval:`templates_path` に存在する独自のテンプレートをリストで指定する。
    リストに記載されたテンプレートファイルが順番にサイドバーに表示される。

.. confval:: html_context
    :type: ``dict[str, Any]``
    :default: ``{}``

    テンプレートエンジンに渡される辞書オブジェクト。
    独自のテンプレートに対してパラメータを渡すために使用できる。

.. confval:: html_theme_options
    :type: ``dict``
    :default: ``{}``

    テーマ固有のオプションの辞書オブジェクト。

.. confval:: html_title
    :type: ``str``
    :default: ``project release documentation``

    HTMLページのタイトル文字列。
    デフォルトは、conf.py の ``project`` ``release`` を元にしたタイトルである。



サイドバーのカスタマイズ
----------------------------

:confval:`html_sidebars` にテンプレートファイルを追加することで、サイドバーの内容を変更できる。
テンプレートファイルは、 Jinja2によって処理される。
基本的な書き方は以下の通り。詳細は、 `公式ドキュメント <https://jinja.palletsprojects.com/en/stable/templates/>`_ を参照のこと。

.. code-block:: html
    :name: code-jinja2
    :caption: Jinja2の基本文法
    :linenos:

    <!-- 変数の値を展開する -->
    {{ 変数名 }}
    {{ 変数名|フィルタ }}

    <!-- コメント -->
    {# コメント #}

    <!-- 条件分岐 -->
    {% if 条件式 %}

    {% elif 条件式 %}

    {% else %}

    {% endif %}

    <!-- forループによりリスト変数を展開する -->
    {% for 変数名 in リスト変数 %}
        {{ 変数名 }}
    {% endfor %}

    <!-- 継承 -->
    <!--  親テンプレート -->
    {% block ブロック名 %}
    
    {% endblock %}

    <!-- 子テンプレート -->
    {% extends "親テンプレート" %}
    {% block ブロック名 %}
        置き換える内容
    {% endblock %}
    {% block ブロック名 %}
        {{ super() }}
        追加する内容
    {% endblock %}

    <!-- マクロ -->
    {% macro マクロ名(引数1, 引数2=デフォルト値) %}
        {{ 引数1 }}
        {{ 引数2 }}
    {% endmacro %}


サイドバーテンプレートに使用できる変数の一部を :numref:`tab-templates-variables` に示す。
このリストは、Furo theme の使用を前提に ``{{ debug() }}`` を実行したときに表示される変数一覧から抜粋したものである。
これ以外に、今回抜粋していない変数、拡張機能が定義する変数、 :confval:`html_context` で定義した変数ある。

.. csv-table:: サイドバーテンプレートで使用できる変数名(抜粋)
    :name: tab-templates-variables
    :header-rows: 1
    :widths: 2,2,2

    変数名, 説明, 例
    project, プロジェクト名( conf.py の ``project`` ), 
    release, リリース( conf.py の ``release`` ), 
    version, バージョン( conf.py の ``version`` ), 
    last_updated, 最終更新日( conf.py の ``html_last_updated_fmt`` に基づく表記), 
    copyright, コピーライト( conf.py の ``copyright`` )
    docstitle, タイトル( conf.py の ``html_title`` )
    shorttitle, ショートタイトル( conf.py の ``html_short_title`` )
    language, 言語( conf.py の ``language`` ), ja
    root_doc, ルートドキュメントの名前, index
    rellinks, 現在のページの関連ページに関するタプルリスト, "[('genindex','総合索引','I','索引'),('sample/theme','2. テーマカスタマイズ','N','次へ'),('index','Sphinxメモ','P','前へ')]"
    theme_sidebarwidth, テーマのサイドバーの幅, 230
    theme_body_min_width, テーマ本文の幅(最小), 360
    theme_body_max_width, テーマ本文の幅(最大), 800
    theme_dark_css_variables [#vfuro]_ , ダークテーマ固有のスタイル変数, "{'color-brand-primary': '#FFBB00','color-brand-content': '#FFFF99'}"
    theme_light_css_variables [#vfuro]_ , ライトテーマ固有のスタイル変数, "{'color-brand-primary': '#CC6600','color-brand-content': '#CC8844'}"
    prev, 前ページに関する情報, "{'link': '../index.html','title': 'Sphinxメモ'}"
    next, 次のページに関する情報 "{'link': 'theme.html','title': '2. テーマカスタマイズ'}"
    title, 現在のページのタイトル, "2. HTMLのカスタマイズ"
    body, 本文の内容,
    furo_pygments [#vfuro]_ , Furo theme Pygmentsの設定, "{'light': {'background': '#f2f2f2','foreground': '#1e1e1e'},'dark': {'background': '#202020','foreground': '#d0d0d0'}}"

.. [#vfuro] Furo theme 適用時に使える変数

例： ナビゲーションエリア

次のページ/前のページに移動するためのボタンをサイドバーに表示する例を示す。
この中では、テンプレート変数の使用、Furo Theme の

.. literalinclude:: /_template/sidebar/step_navs.html
    :name: code-example-step-navs
    :caption: _template/sidebar/step_navs.html
    :language: html



公開
-----------------