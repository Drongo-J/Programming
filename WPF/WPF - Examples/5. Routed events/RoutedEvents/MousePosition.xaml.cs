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

namespace RoutedEvents
{
    /// <summary>
    /// Interaction logic for MousePosition.xaml
    /// </summary>

    public partial class MousePosition : System.Windows.Window
    {

        public MousePosition()
        {
            InitializeComponent();
        }

        private void MouseMoved(object sender, MouseEventArgs e)
        {
            Point pt = e.GetPosition(this);
            lblInfo.Text = 
                String.Format("You are at ({0},{1}) in window coordinates",
                pt.X, pt.Y);            
        }
 
    }
}