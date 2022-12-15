using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace Resources_Example
{
    /// <summary>
    /// Interaction logic for DynamicResource.xaml
    /// </summary>
    public partial class DynamicResource : Window
    {
        public DynamicResource()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                ImageBrush brush = (ImageBrush)this.Resources["TileBrush"];
                brush.Viewport = new Rect(0, 0, 5, 5);
            }
            catch
            { } 
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
           
            this.Resources["TileBrush"] = new SolidColorBrush(Colors.LightBlue);
        }

    }
}
