import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


valid_email = "selenium.projekt@wp.pl"
valid_password = "55!klony"
invalid_password = "55klony"
valid_address_mail = "turquss@wp.pl"
valid_topic_mail = "Projekt zaliczeniowy Selenium"
textMail = "Dzien dobry , wysyłam projekt Selenium na zaliczenie"



class WpPocztaMail(unittest.TestCase):
    # Warunki wstępne testów
    def setUp(self):
        print("Przygotowanie testu")
        # Tutaj właczymy przeglądarkę
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        # Wejdziemy na stronę poczty wp
        self.driver.maximize_window()
        self.driver.get('https://profil.wp.pl/login.html?zaloguj=poczta')

    # Instrukcje po każdym teście
    def tearDown(self):
        print("Sprzątanie po teście")
        # Wyłączamy przeglądarkę
        self.driver.quit()

    @unittest.skip("pomijam")
    def testEmailLogging(self):
        print("Prawdziwy test")
        # KROK 1 : Wpisz poprawny adres i haslo
        driver = self.driver
        email_input = driver.find_element_by_name('login_username')
        email_input.send_keys(valid_email)
        time.sleep(4)
        password_input = driver.find_element_by_name('password')
        password_input.send_keys(valid_password)
        time.sleep(4)
        # KROK 2: Zaloguj
        login_btn = self.driver.find_element_by_xpath('//button[@type="submit"]')
        login_btn.click()

        # KROK  : Jesli wyskoczy strona z komunikatem to pomiń
       # statement_btn = self.driver.find_element_by_xpath('//button[@class="sc-ifAKCX sc-kfGgVZ sc-GMQeP btHNAj"]')
        #if statement_btn:
         #   statement_btn.click()
        #else:
         #   write_input = driver.find_element_by_xpath('//button[@href="#/draft?type=new"]')
          #  write_input.click()

        # KROK  : Znajdz element 'napisz' i kliknij
        write_input = driver.find_element_by_xpath('//button[@href="#/draft?type=new"]')
        write_input.click()
        # KROK  : napisz wiadomosc
        text_box = driver.find_element_by_xpath('//div[@class="DraftEditor-editorContainer"]')

        # wprowadzam text z innego pliku
        text_box.send_keys(textMail)

        # KROK  : Wpisz adres mailowy i temat wiadomosci
        address_mail = driver.find_element_by_xpath('//input[@class="sc-dznXNo dQOuJH"]')
        address_mail.send_keys(valid_address_mail)
        topic_mail = driver.find_element_by_xpath('//input[@class="sc-hMqMXs gzmkJt"]')
        topic_mail.send_keys(valid_topic_mail)

        #sprawdz poprawnosc zalogowania poprzez email nadawcy, czy sie zgadza
        email_fact = driver.find_element_by_xpath('//div[@class="shrink-none change-sender-name"]').get_attribute('innerText')
        print("W polu jest email: ", email_fact)
        assert valid_email == email_fact
        self.assertEqual(valid_email, email_fact)

        #sprawdzenie czy tresc maila zostala poprawnie wprowadzona
        text_box_fact = driver.find_element_by_xpath('//div[@class="DraftEditor-editorContainer"]/div').get_attribute('innerText')
        print("Wiadomosc wysylana brzmi: ", text_box_fact)
        assert textMail == text_box_fact
        self.assertEqual(textMail, text_box_fact)
        # KROK  : Wyslij wiadomosc
        send_btn = driver.find_element_by_xpath('//div[@class="sc-hizQCF CEtqc"]')
        send_btn.click()

        # KROK  : Wyloguj
        logout_btn = driver.find_element_by_xpath('//button[@class="Button topuser__logout"]')
        logout_btn.click()



    @unittest.skip("pomijam")
    def testInvalidEmailLogging(self):
        print("Prawdziwy test")
        # KROK 1 : Wpisz poprawny adres i haslo
        driver = self.driver
        email_input = driver.find_element_by_name('login_username')
        email_input.send_keys(valid_email)
        time.sleep(4)
        password_input = driver.find_element_by_name('password')
        password_input.send_keys(invalid_password)
        time.sleep(4)
        # KROK 2: Zaloguj
        login_btn = self.driver.find_element_by_xpath('//button[@type="submit"]')
        login_btn.click()
        time.sleep(4)

        # II TEST
        # Wyszukaj wszystkie możliwe błędy
        # ..find_elements... zwraca LISTĘ WebElementów komunikat bledow po zlym zalogowaniu
        possible_errors = driver.find_elements_by_xpath('//div[@class="notification notification--error"]/span')
        # !!!!!!!!!!!!! Sprawdź, które są widoczne
        # Pusta lista na widoczne błędy
        visible_errors = []
        # Dla każdego błędu w liście possible_errors
        for error in possible_errors:
            # Jelsi błąd jest widoczny
            if error.is_displayed():
                # Dodaj go do listy widocznych
                visible_errors.append(error)

        self.assertEqual(len(visible_errors), 2)  # metoda unittestowa
          # !!!!!!!!!!!!!!!! Sprawdź, czy treść jest poprawna: "Nieprawidłowy adres e-mail"
        print("Tekst błędu na stronie: ", visible_errors[0].text)
        self.assertEqual(visible_errors[0].text,"Podany login i/lub hasło są nieprawidłowe.")

        time.sleep(4)

    #@unittest.skip("pomijam")
    def testEmptyMail(self):
        print("Prawdziwy test")
        # KROK 1 : Wpisz poprawny adres i haslo
        driver = self.driver
        email_input = driver.find_element_by_name('login_username')
        email_input.send_keys(valid_email)

        password_input = driver.find_element_by_name('password')
        password_input.send_keys(valid_password)
        # KROK 2: Zaloguj
        login_btn = self.driver.find_element_by_xpath('//button[@type="submit"]')
        login_btn.click()


        # KROK  : Znajdz element 'napisz' i kliknij
        write_input = driver.find_element_by_xpath('//button[@href="#/draft?type=new"]')
        write_input.click()
        # KROK  : nie wpisujemy tresci
        #text_box = driver.find_element_by_xpath('//div[@class="DraftEditor-editorContainer"]')

        # nie wprowadzam tekstu z innego pliku
        #text_box.send_keys(textMail)

        # KROK  : Wpisz adres mailowy i temat wiadomosci
        #address_mail = driver.find_element_by_xpath('//input[@class="sc-kEmuub cvKTPD"]')
        address_mail = driver.find_element_by_xpath('//input[@class="sc-dznXNo dQOuJH"]')
        address_mail.send_keys(valid_address_mail)
        topic_mail = driver.find_element_by_xpath('//input[@class="sc-hMqMXs gzmkJt"]')
        topic_mail.send_keys(valid_topic_mail)

        # KROK  : Wyslij wiadomosc
        send_btn = driver.find_element_by_xpath('//div[@class="sc-hizQCF CEtqc"]')
        send_btn.click()

        message_send = driver.find_element_by_xpath('//div[@class="sc-dRCTWM kxlYhQ"]')

        print(message_send.get_attribute('innerText'))
        self.assertEqual(message_send.is_displayed(), True)
        assert message_send.is_displayed() == True
        # KROK  : Wyloguj
        logout_btn = driver.find_element_by_id('Logout-Button')
        logout_btn.click()
        time.sleep(1)



# Jeśli uruchamiamy z tego pliku
if __name__=="__main__":
    # Włączamy testy
    unittest.main()
