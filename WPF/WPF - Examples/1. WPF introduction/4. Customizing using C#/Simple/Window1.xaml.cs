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

namespace Simple
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
        public Window1()
        {
            InitializeComponent();
            LinearGradientBrush brush = new LinearGradientBrush();
            GradientStop gradientStop1 = new GradientStop();
            gradientStop1.Offset = 0;
            gradientStop1.Color = Colors.Red;
            brush.GradientStops.Add(gradientStop1);
            GradientStop gradientStop2 = new GradientStop();
            gradientStop2.Offset = 0.5;
            gradientStop2.Color = Colors.Indigo;
            brush.GradientStops.Add(gradientStop2);
            GradientStop gradientStop3 = new GradientStop();
            gradientStop3.Offset = 1;
            gradientStop3.Color = Colors.Violet;
            brush.GradientStops.Add(gradientStop3);
            grid1.Background = brush; 
        }

        private void cmdAnswer_Click(object sender, RoutedEventArgs e)
        {
            txt2.Text = txt1.Text;
        }
    }
}
