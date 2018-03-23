import fetchme

# --- create object for scihub queries
obj = fetchme.Scihub()

# - scihub authentification
f = file('./conf/credentials_scihub.txt')
(usr, pwd) = f.readline().split(' ')
obj.query_auth(usr, pwd)

# --- read config file
# conffile = '_config_etna_archive.yml'
# obj.read_configfile('./conf/' + conffile)
# print obj.cfg['optn_download']

# --- set logging behaviour
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
logging.getLogger('requests').setLevel(logging.ERROR)
logging.info('>> script started')


# =============================================
# QUERY
# =============================================

# --- print scihub query url
# productlist = obj.scihub_search(print_url=1)

# --- doc with all options for scihub query:
# see ./conf/config_options.txt

# --- parse options from kwargs
# - ex: filename:
# obj.scihub_search(filename='S1*')
# - ex: footprint WKT format (http://boundingbox.klokantech.com/)
# obj.scihub_search(footprint='POLYGON((-2.211 49.9654, -0.835 49.9654, -0.835 49.1206, -2.211 49.1206, -2.211 49.9654))')

# --- parse options from dict
optns = {'filename': 'S1A*', 'maxrecords': 5}

optns = dict(
    platformname='Sentinel-1',
    producttype='SLC',
    sensoroperationalmode='IW',
    maxrecords=5)

obj.scihub_search(**optns)

# --- parse options from yaml configuration file
# obj.scihub_search(configfile='./conf/_config_ertaale.yml')

# -- parse options from loaded yaml configration file
# obj.read_configfile('./conf/_config_ertaale.yml')
# obj.scihub_search()

# -- examples:
# ex: cloud coverage
# pl = obj.scihub_search(filename='S2*', cloudcoverpercentage='[0 TO 25]', footprint=[-1.5578, 29.4729])

# ex: search specific file
# productlist = obj.scihub_search(filename='S1A_IW_SLC__1SDV_20170507T050422_20170507T050449_016471_01B4A7_9DF7*')

# ex: print url, export results as xml
# obj.scihub_search(configfile='./conf/_config_pitonfournaise_archive.yml', print_url=1, export_result=1)

# === filter results on the fly (default=by intersection percentage with footprint)
# productlist = obj.scihub_search(
#     footprint=footprint,
#     filter_tiles=1)

# =============================================
# ANALYZE QUERY output
# =============================================

# --- get product metadata
# print(productlist[0].metadata)
# print productlist[0].metadata['title']

# --- get product md5sum
# productlist[0].getMd5sum()

# --- plot product footprint
# productlist[0].plotFootprint()
# productlist[0].plotFootprint(wkt2plot_xtra=footprint)
# productlist[0].plotFootprint(wkt2plot_xtra=footprint, plot_country='Ethiopia', f_out='oulala')
#
# --- plot all products' footprint
# TODO: create class for productlist, and assign plot_footprints as a method (like 'plotFootprint' method for single product)
# productlist = obj.scihub_search(
#   plot_footprints=1,
#   **s2_optn)

# --- plot tile of each product in list
# obj.print_product_title(productlist)

# --- filter productlist (default=filter when several products have same acq time, select tile havest largest area with aoi footprint)
# productlist_filt, productlist_dropped = obj.productlist_filter(productlist, aoi_footprint=footprint, filter_method='intersection_with_aoi')
# print('FILTERED results:')
# obj.print_product_title(productlist_filt)

# --- find products stored/not stored in DB_MOUNTS:
# dbo = utilme.Database()
# p_inDB, p_noDB = dbo.dbmounts_isproduct_archived(p)
# fetchme.Scihub().print_product_title(p_noDB)  # +> print products not found in DB

# =============================================
# DOWNLOAD
# =============================================

# --- get product quicklook
# productlist[0].getQuicklook()

# --- get full product
# productlist[0].getFullproduct()

# --- get full product specify download dir
# productlist[0].getFullproduct(download_dir='/home/sebastien/DATA/data_satellite/etna')

# --- get full product + force not to check file integrity if file is found
# productlist[0].getFullproduct(download_dir='/home/sebastien/DATA/data_satellite/etna', check_md5sum=False)

# --- scihub download
# obj.scihub_download(productlist)
