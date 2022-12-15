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

namespace StackPanel_sample
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
        public Window1()
        {
            InitializeComponent();
            this.Title = "StackPanel Sample";
            //StackPanel располагает дочерние элементы в одну строку, которую можно ориентировать по горизонтали или по вертикали
            StackPanel myStackPanel = new StackPanel();
       
            // Define the child content
            Border myBorder1 = new Border();
            myBorder1.Background = Brushes.SkyBlue;
            myBorder1.BorderBrush = Brushes.Black;
            myBorder1.BorderThickness = new Thickness(1);
            TextBlock myTextBlock1 = new TextBlock();
            myTextBlock1.Foreground = Brushes.Black;
            myTextBlock1.FontSize = 12;
            myTextBlock1.Text = "Stacked Item #1";
            myBorder1.Child = myTextBlock1;

            // Define the child content
            Border myBorder2 = new Border();
            myBorder2.Background = Brushes.CadetBlue;
            myBorder2.BorderBrush = Brushes.Black;
            myBorder2.BorderThickness = new Thickness(1);
            TextBlock myTextBlock2 = new TextBlock();
            myTextBlock2.Foreground = Brushes.Black;
            myTextBlock2.FontSize = 14;
            myTextBlock2.Text = "Stacked Item #2";
            myBorder2.Child = myTextBlock2;


            // Define the child content
            Border myBorder3 = new Border();
            myBorder3.Background = Brushes.LightGoldenrodYellow;
            myBorder3.BorderBrush = Brushes.Black;
            myBorder3.BorderThickness = new Thickness(1);
            TextBlock myTextBlock3 = new TextBlock();
            myTextBlock3.Foreground = Brushes.Black;
            myTextBlock3.FontSize = 16;
            myTextBlock3.Text = "Stacked Item #3";
            myBorder3.Child = myTextBlock3;


            // Define the child content
            Border myBorder4 = new Border();
            myBorder4.Width = 200;
            myBorder4.Background = Brushes.PaleGreen;
            myBorder4.BorderBrush = Brushes.Black;
            myBorder4.BorderThickness = new Thickness(1);
            TextBlock myTextBlock4 = new TextBlock();
            myTextBlock4.Foreground = Brushes.Black;
            myTextBlock4.FontSize = 18;
            myTextBlock4.Text = "Stacked Item #4";
            myBorder4.Child = myTextBlock4;

            // Define the child content
            Border myBorder5 = new Border();
            myBorder5.Background = Brushes.White;
            myBorder5.BorderBrush = Brushes.Black;
            myBorder5.BorderThickness = new Thickness(1);
            TextBlock myTextBlock5 = new TextBlock();
            myTextBlock5.Foreground = Brushes.Black;
            myTextBlock5.FontSize = 20;
            myTextBlock5.Text = "Stacked Item #5";
            myBorder5.Child = myTextBlock5;


            // Add child elements to the DockPanel Children collection
            myStackPanel.Children.Add(myBorder1);
            myStackPanel.Children.Add(myBorder2);
            myStackPanel.Children.Add(myBorder3);
            myStackPanel.Children.Add(myBorder4);
            myStackPanel.Children.Add(myBorder5);

            // Add the parent Canvas as the Content of the Window Object
            this.Content = myStackPanel;
        }
    }
}
