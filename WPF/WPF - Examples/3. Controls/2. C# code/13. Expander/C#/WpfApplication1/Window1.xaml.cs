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
            Expander MyControl = new Expander();
            MyControl.Header = "Дополнительно";
            StackPanel Stack = new StackPanel() { Margin = new Thickness(6) };
            TextBox MyTextBox = new TextBox() { Margin = new Thickness(6) };
            Button MyButton = new Button() { Margin = new Thickness(6) };
            MyButton.Content = "Ok";
            Stack.Children.Add(MyTextBox);
            Stack.Children.Add(MyButton);
            MyControl.Content = Stack;
            grid1.Children.Add(MyControl);

        }
    }
}
