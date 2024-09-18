using System;
using System.IO;
using System.Windows;
using System.Windows.Media.Imaging;

namespace Egzamin
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }
        private void TbNumer_TextChanged(object sender, System.Windows.Controls.TextChangedEventArgs e)
        {
            string numer = tbNumer.Text;
            if (numer.Length > 0)
            {
                string zdjeciePlik = $"{numer}-zdjecie.jpg";
                string odciskPlik = $"{numer}-odcisk.jpg";

                if (File.Exists(zdjeciePlik))
                {
                    pbZdjecie.Source = new BitmapImage(new Uri(Path.GetFullPath(zdjeciePlik)));
                }
                else
                {
                    pbZdjecie.Source = null;
                }

                if (File.Exists(odciskPlik))
                {
                    pbOdcisk.Source = new BitmapImage(new Uri(Path.GetFullPath(odciskPlik)));
                }
                else
                {
                    pbOdcisk.Source = null;
                }
            }
            else
            {
                pbZdjecie.Source = null;
                pbOdcisk.Source = null;
            }
        }

        private void BtnOK_Click(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrWhiteSpace(tbImie.Text) || string.IsNullOrWhiteSpace(tbNazwisko.Text))
            {
                MessageBox.Show("Wprowadź dane");
            }
            else
            {
                string kolorOczu = rbNiebieskie.IsChecked == true ? "niebieski" :
                                   rbZielone.IsChecked == true ? "zielony" :
                                   rbPiwne.IsChecked == true ? "piwny" : "";
                MessageBox.Show($"{tbImie.Text} {tbNazwisko.Text} kolor oczu {kolorOczu}");
            }
        }
    }
}
