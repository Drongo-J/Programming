using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
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
            ScrollBar MyControl = new ScrollBar();
            MyControl.Name = "ScrollBar1";
            MyControl.Minimum = 0;
            MyControl.Maximum = 100;
            MyControl.Value = 50;
            MyControl.Orientation = Orientation.Horizontal;
            MyControl.Margin = new Thickness(10, 30, 10, 10);
            grid.Children.Add(MyControl);

        }
    }
}
