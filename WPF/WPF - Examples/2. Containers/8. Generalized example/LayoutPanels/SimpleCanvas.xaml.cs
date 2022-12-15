using System;
using System.Collections.Generic;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace LayoutPanels
{
    /// <summary>
    /// Interaction logic for SimpleCanvas.xaml
    /// </summary>

    public partial class SimpleCanvas : System.Windows.Window
    {

        public SimpleCanvas()
        {
            InitializeComponent();
        }

        private void btn1_Click(object sender, RoutedEventArgs e)
        {
            Canvas.SetZIndex(btn1, 1);
            Canvas.SetZIndex(btn2, 0);
        }

        private void btn2_Click(object sender, RoutedEventArgs e)
        {
            Canvas.SetZIndex(btn1, 0);
            Canvas.SetZIndex(btn2, 1);
        }

    }
}