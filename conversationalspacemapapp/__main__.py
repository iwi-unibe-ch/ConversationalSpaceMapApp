import conversationalspacemapapp.App.TogaApp.app as TogaApp


def main(toga=True):
    if toga:
        TogaApp.main().main_loop()
    else:
        NotImplemented("No other GUI implementation available.")


if __name__ == "__main__":
    main()
