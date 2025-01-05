from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication
from zapzap.services.DictionariesManager import DictionariesManager


class PageGeneral(QWidget):
    """Gerencia a página de configurações gerais de aparência e idioma."""

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("zapzap/ui/ui_page_general.ui", self)
        self._load_settings()
        self._configure_signals()

    def _load_settings(self):
        """
        Carrega as configurações iniciais para a interface:
        - Exibe o caminho dos dicionários.
        - Popula o combobox com os idiomas disponíveis.
        - Define o idioma atualmente configurado.
        """
        dictionaries_path = DictionariesManager.get_path()
        self.dic_path.setText(dictionaries_path)
        self.spell_comboBox.addItems(DictionariesManager.list())

        system_language = DictionariesManager.get_system_language()
        current_language = DictionariesManager.get_current_dict()

        print(f"Caminho dos dicionários: {dictionaries_path}")
        print(f"Idioma do sistema: {system_language}")
        print(f"Idioma atual configurado: {current_language}")

        self.spell_comboBox.setCurrentText(current_language)

    def _configure_signals(self):
        """
        Configura os sinais dos widgets:
        - Conecta o combobox de idiomas ao manipulador de mudança de idioma.
        """
        self.spell_comboBox.textActivated.connect(self._handle_spellcheck)

    def _handle_spellcheck(self, lang: str):
        """
        Manipula a mudança de idioma para o corretor ortográfico.
        Atualiza a configuração e notifica o navegador.

        Args:
            lang (str): Idioma selecionado.
        """
        print(f"Linguagem selecionada: {lang}")
        DictionariesManager.set_lang(lang)
        QApplication.instance().getWindow().browser.update_spellcheck()
