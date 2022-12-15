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

namespace ClassicControls
{
    /// <summary>
    /// Interaction logic for SliderTest.xaml
    /// </summary>

    public partial class SliderTest : System.Windows.Window
    {

        public SliderTest()
        {
            InitializeComponent();
        }

        private void Slider_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            Slider obj = (Slider) sender;
            this.Title = obj.Value.ToString();
        }

        


    }
}