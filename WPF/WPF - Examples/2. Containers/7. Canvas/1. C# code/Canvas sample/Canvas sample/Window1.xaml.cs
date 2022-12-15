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

namespace Canvas_sample
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
        public Window1()
        {
            InitializeComponent();
            // Определяет область, в рамках которой можно явно расположить дочерние элементы путем использования координат, являющихся относительными к области Canvas
            // Create a canvas sized to fill the window
            this.Title = "Canvas Sample";
            Canvas myCanvas = new Canvas();
            myCanvas.Background = Brushes.LightSteelBlue;

            // Add a "Hello World!" text element to the Canvas
            TextBlock txt1 = new TextBlock();
            txt1.FontSize = 14;
            txt1.Text = "Hello World!";
            Canvas.SetTop(txt1, 100);
            Canvas.SetLeft(txt1, 10);
            myCanvas.Children.Add(txt1);

            // Add a second text element to show how absolute positioning works in a Canvas
            TextBlock txt2 = new TextBlock();
            txt2.FontSize = 22;
            txt2.Text = "Isn't absolute positioning handy?";
            Canvas.SetTop(txt2, 200);
            Canvas.SetLeft(txt2, 75);
            myCanvas.Children.Add(txt2);
            this.Content = myCanvas;
        }
    }
}
