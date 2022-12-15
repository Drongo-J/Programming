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
            Label MyControl = new Label();
            MyControl.Name = "MyControl";
            MyControl.Content = "You Name";
            MyControl.Background = new SolidColorBrush(Color.FromRgb(255, 255, 0));
            MyControl.Margin = new Thickness(50, 50, 0, 0);
            grid.Children.Add(MyControl);

        }
    }
}
