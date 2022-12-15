namespace WindowsFormsApp6._1
{
    partial class Form2
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.productsListbx = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // productsListbx
            // 
            this.productsListbx.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.productsListbx.FormattingEnabled = true;
            this.productsListbx.ItemHeight = 25;
            this.productsListbx.Location = new System.Drawing.Point(12, 12);
            this.productsListbx.Name = "productsListbx";
            this.productsListbx.Size = new System.Drawing.Size(463, 429);
            this.productsListbx.TabIndex = 0;
            this.productsListbx.DoubleClick += new System.EventHandler(this.productsListbx_DoubleClick);
            // 
            // Form2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(487, 450);
            this.Controls.Add(this.productsListbx);
            this.Name = "Form2";
            this.Text = "Form2";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListBox productsListbx;
    }
}