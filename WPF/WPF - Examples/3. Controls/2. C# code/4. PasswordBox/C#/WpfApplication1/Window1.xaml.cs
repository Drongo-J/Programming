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
            PasswordBox MyControl = new PasswordBox();
            MyControl.Name = "MyControl";
            MyControl.Password = "SuperText";
            MyControl.Margin = new Thickness(20, 20, 0, 0);
            MyControl.Width = 100;
            MyControl.Height = 24;
            grid.Children.Add(MyControl);

        }
    }
}
