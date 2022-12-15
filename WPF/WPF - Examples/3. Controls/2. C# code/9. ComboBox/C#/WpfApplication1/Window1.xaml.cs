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
            ComboBox MyControl = new ComboBox();
            MyControl.Name = "ComboBox1";
            MyControl.Margin = new Thickness(30);
            MyControl.Items.Add("BMW");
            MyControl.Items.Add("Ferrari");
            MyControl.Items.Add("Ford");
            MyControl.Items.Add("Honda");
            grid.Children.Add(MyControl);
        }
    }
}
