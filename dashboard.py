import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def getTopSeller(N):
    topselling_seller = pd.read_csv("topselling_seller.csv")
    seller_city = pd.read_csv("seller_city.csv")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    top10_seller = topselling_seller.head(N)
    ax1.bar(top10_seller["seller_id"], top10_seller["total"])
    ax1.set_xlabel("Seller City")
    ax1.set_ylabel("Total")
    ax1.set_title("Top {} Seller".format(N))
    ax1.set_xticklabels(top10_seller["seller_city"], rotation=90)

    top10_seller_city = seller_city.head(10)
    ax2.bar(top10_seller_city["seller_city"], top10_seller_city["total"])
    ax2.set_xlabel("Seller City")
    ax2.set_ylabel("Total")
    ax2.set_title("Top {} Seller City".format(10))
    ax2.set_xticklabels(top10_seller_city["seller_city"], rotation=90)

    st.pyplot(fig)

    fig, ax3 = plt.subplots()

    

    top10_seller = topselling_seller.head(N)
    top10_seller = top10_seller.groupby("seller_city").size().sort_values(ascending=False).reset_index(name="total")
    ax3.pie(top10_seller["total"], labels=top10_seller["seller_city"], autopct="%1.1f%%")
    ax3.set_title("City Distribution of Top {} Seller".format(N))

    st.pyplot(fig)

st.header("Dicoding Submission Dashboard")

with st.sidebar:
    st.text('Dicoding Submission Dashboard')
    st.text('By: Diky Wahyudi')

    st.markdown("[Explore Daerah manakah yang memiliki pengguna terbanyak dan apa produk yang paling banyak dipesan oleh pengguna ?](#explore-daerah-manakah-yang-memiliki-pengguna-terbanyak-dan-apa-produk-yang-paling-banyak-dipesan-oleh-pengguna)")

    st.markdown("[Seller manakah yang memiliki penjualan terbanyak dan darimanakah mereka berasal ?](#seller-manakah-yang-memiliki-penjualan-terbanyak-dan-darimanakah-mereka-berasal)")

    st.markdown("[Apakah metode pembayaran yang paling banyak digunakan ?](#apakah-metode-pembayaran-yang-paling-banyak-digunakan)")

with st.expander("Daerah manakah yang memiliki pengguna terbanyak dan apa produk yang paling banyak dipesan oleh pengguna ?"):
    st.subheader("Explore Daerah manakah yang memiliki pengguna terbanyak dan apa produk yang paling banyak dipesan oleh pengguna ?")

    data_customer = pd.read_csv("data_cust.csv")
    top10_cust_city = data_customer.groupby("customer_city").size().sort_values(ascending=False).reset_index(name="total").head(10)

    best_selling_sao_paulo = pd.read_csv("best_selling_sao_paulo.csv")
    best_selling_rio_de_janeiro = pd.read_csv("best_selling_rio_de_janeiro.csv")
    best_selling_belo_horizonte = pd.read_csv("best_selling_belo_horizonte.csv")

    top10_sao_paulo = best_selling_sao_paulo.head(10)
    top10_rio_de_janeiro = best_selling_rio_de_janeiro.head(10)
    top10_belo_horizonte = best_selling_belo_horizonte.head(10)

    fig, ax = plt.subplots()
    ax.barh(top10_cust_city["customer_city"], top10_cust_city["total"], color="skyblue")
    ax.invert_yaxis()
    ax.set_xlabel("Total")
    ax.set_title("Top 10 Customer City")

    st.pyplot(fig)

    st.write(
        """
        Dari grafik diatas dapat disimpulkan bahwa pelanggan terbanyak berasal dari kota **sao paulo** dan diikuti oleh kota **rio de janeiro** pada posisi kedua dan kota **belo horizonte** pada posisi ke tiga.
        """
    )

    fig, ax = plt.subplots()
    ax.barh(top10_sao_paulo["product_category_name"], top10_sao_paulo["total"])
    ax.invert_yaxis()
    ax.set_xlabel("Total")
    ax.set_title("Top 10 Best Selling Product in Sao Paulo")

    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.barh(top10_rio_de_janeiro["product_category_name"], top10_rio_de_janeiro["total"])
    ax.invert_yaxis()
    ax.set_xlabel("Total")
    ax.set_title("Top 10 Best Selling Product in Rio De Janeiro")

    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.barh(top10_belo_horizonte["product_category_name"], top10_belo_horizonte["total"])
    ax.invert_yaxis()
    ax.set_xlabel("Total")
    ax.set_title("Top 10 Best Selling Product in Belo Horizonte")

    st.pyplot(fig)

    st.write(
        """
            Sebelumnya telah didapatkan kota yang memiliki pelanggan terbanyak yaitu kota san paulo. Selanjutnya untuk produk yang terlaris dibeli oleh penduduk kota san paulo dapat dilihat pada grafik diatas yang menunjukkan kategori barang terpopuler dibeli oleh penduduk kota sao paulo adalah **bed bath table**, **health beauty** dan **sport lessure**. Sedangkan pada kota Rio de Janeiro untuk posisi kedua adalah **furniture decor** dan di kota Belo Horizonte untuk posisi ke tiga adalah **computers_accessories** 
        """
    )

with st.expander("Seller manakah yang memiliki penjualan terbanyak dan darimanakah mereka berasal ?"):
    st.subheader("Seller manakah yang memiliki penjualan terbanyak dan darimanakah mereka berasal ?")
    getTopSeller(10)

    st.write(
        """
            Berdasarkan grafik diatas dapat disimpulkan bahwa kota sao paulo memiliki jumlah seller terbanyak dibangingkan dengan kota lainnya. Dan 30% seller dengan jumlah penjualan terbanyak berada di kota sao paulo. Pada gambar grafik ke tiga dapat dilihat jumlah seller yang berada di kota sao paulo sangatlah banyak jika dibandingkan dengan kota lainnya.
        """
    )

with st.expander("Apakah metode pembayaran yang paling banyak digunakan ?"):
    st.subheader("Apakah metode pembayaran yang paling banyak digunakan ?")

    data_pembayaran = pd.read_csv("data_pembayaran.csv")
    data_cicilan = pd.read_csv("data_cicilan.csv")
    
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20, 5))

    ax1.bar(data_pembayaran["payment_type"], data_pembayaran["total"])
    ax1.set_title("Payment Type Distribution for non Installment")

    ax2.bar(data_cicilan["payment_type"], data_cicilan["total"])
    ax2.set_title("Payment Type Distribution for Installment")

    st.pyplot(fig)

    st.write(
        """
            Berdasarkan dari grafik diatas dapat dilihat dari semua transaksi dapat diketahui jenis pembayaran yang paling banyak di minati oleh pelanggan adalah menggunakan kartu kredit,sedangkan pelanggan yang melakukan pembayaran melalui cicilan lebih banyak menggunakan metode pembayaran menggunakan voucher
        """
    )

