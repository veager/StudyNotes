def creat_mesh_grid(x_min, x_max, y_min, y_max, width=200, heigth=200):
    '''
    creat mesh grids
    
    parameters:
    -----------
    x_min, x_max, y_min, y_max (float) : a rectangular boundary, 
        left-bottom point (x_min, y_min) ->  right-top point (x_max, y_max)
    width, heigth (flaot) : the width and heigh of the grid
        
    Return:
    -------
    grid_gpd (geopandas.GeoDataFrame) :
    '''
    from shapely.geometry import Polygon
    
    grid_li = []
    
    n_row = int((x_max - x_min) // width + 1)
    n_col = int((y_max - y_min) // heigth + 1)
    
    for i in range(n_row):
        for j in range(n_col):
            x_1 = x_min + i * width
            y_1 = y_min + j * heigth
            
            polygon = Polygon([(x_1, y_1), (x_1+width, y_1), (x_1+width, y_1+heigth), (x_1, y_1+heigth)])
            grid_li.append(polygon)
    
    grid_gpd = gpd.GeoSeries(grid_li)
    grid_gpd = gpd.GeoDataFrame(grid_gpd.area, columns=['Area'], geometry=grid_gpd.geometry)
    # print(n_row*n_col, grid_gpd.shape[0])
    return grid_gpd
# =================================================


def mesh_grid_mask(grid_gpd, boundary_geo):
    '''
    based on boundary ("boundary_geo"), screen grids ("grid_gpd"). 
    Only those grids intersect with "boundary_geo" will be reserved.
    
    parameters:
    -----------
    grid_gpd (geopandas.GeoDataFrame) : 
    boundary_geo (shapely.geometry.Polygon):
        
    Return:
    -------
    grid_gpd(geopandas.GeoDataFrame) :
    '''
    
    grid_gpd['flag'] = grid_gpd.intersects(boundary_geo)
    
    # select out
    grid_gpd = grid_gpd[grid_gpd['flag']]
    
    grid_gpd = grid_gpd.drop('flag', axis=1)
    
    # reset_index
    grid_gpd = grid_gpd.reset_index(drop=True)
    grid_gpd['grid_id'] = grid_gpd.index.to_list()
    
    return grid_gpd
# =================================================
