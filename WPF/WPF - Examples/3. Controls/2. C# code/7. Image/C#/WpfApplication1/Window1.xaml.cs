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
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApplication1
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
        public Window1()
        {
            InitializeComponent();
            Image image1 = new Image();
            BitmapImage myBitmapImage = new BitmapImage(new Uri("Image/Chrysanthemum.jpg", UriKind.Relative));
            image1.Source = myBitmapImage;
            grid.Children.Add(image1);
        }
    }
}
