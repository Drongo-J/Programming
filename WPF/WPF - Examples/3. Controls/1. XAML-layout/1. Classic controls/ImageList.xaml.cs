using System;
using System.Collections.Generic;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace ClassicControls
{
    /// <summary>
    /// Interaction logic for ImageList.xaml
    /// </summary>

    public partial class ImageList : System.Windows.Window
    {

        public ImageList()
        {
            InitializeComponent();
        }
        private void lst_SelectionChanged(object sender, RoutedEventArgs e)
        {
            ListBox list = (ListBox)e.Source;
            StackPanel item = (StackPanel)list.SelectedItem;
            Label l = (Label) item.Children[1];
            MessageBox.Show(l.Content.ToString());
        }
    }
}