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
            RadioButton MyControl1 = new RadioButton();
            MyControl1.Name = "MyControl1";
            MyControl1.Content = "Radio1";
            MyControl1.Margin = new Thickness(20, 20, 0, 0);
            MyControl1.Width = 200;
            MyControl1.Height = 24;
            MyControl1.GroupName = "Group1";
            RadioButton MyControl2 = new RadioButton();
            MyControl2.Name = "MyControl2";
            MyControl2.Content = "Radio2";
            MyControl2.Margin = new Thickness(20, 20, 0, 0);
            MyControl2.Width = 200;
            MyControl2.Height = 24;
            MyControl2.GroupName = "Group1";
            MyControl2.IsChecked = true;
            RadioButton MyControl3 = new RadioButton();
            MyControl3.Name = "MyControl3";
            MyControl3.Content = "Radio3";
            MyControl3.Margin = new Thickness(20, 20, 0, 0);
            MyControl3.Width = 200;
            MyControl3.Height = 24;
            MyControl3.GroupName = "Group1";
           

            RadioButton MyControl4 = new RadioButton();
            MyControl4.Name = "MyControl4";
            MyControl4.Content = "Radio4";
            MyControl4.Margin = new Thickness(20, 20, 0, 0);
            MyControl4.Width = 200;
            MyControl4.Height = 24;
            MyControl4.GroupName = "Group2";
            RadioButton MyControl5 = new RadioButton();
            MyControl5.Name = "MyControl5";
            MyControl5.Content = "Radio5";
            MyControl5.Margin = new Thickness(20, 20, 0, 0);
            MyControl5.Width = 200;
            MyControl5.Height = 24;
            MyControl5.GroupName = "Group2";
            MyControl5.IsChecked = true;
            RadioButton MyControl6 = new RadioButton();
            MyControl6.Name = "MyControl6";
            MyControl6.Content = "Radio6";
            MyControl6.Margin = new Thickness(20, 20, 0, 0);
            MyControl6.Width = 200;
            MyControl6.Height = 24;
            MyControl6.GroupName = "Group2"; 
            
            stack.Children.Add(MyControl1);
            stack.Children.Add(MyControl2);
            stack.Children.Add(MyControl3);
            stack.Children.Add(MyControl4);
            stack.Children.Add(MyControl5);
            stack.Children.Add(MyControl6);

        }
    }
}
