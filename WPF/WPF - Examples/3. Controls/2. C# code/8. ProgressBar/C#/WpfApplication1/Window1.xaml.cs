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
            ProgressBar MyControl = new ProgressBar();
            MyControl.Name = "ProgressBar1";
            MyControl.Minimum = 0;
            MyControl.Maximum = 100;
            MyControl.Value = 50;
            MyControl.Margin = new Thickness(5, 30, 5, 30);
            grid.Children.Add(MyControl);

        }
    }
}
