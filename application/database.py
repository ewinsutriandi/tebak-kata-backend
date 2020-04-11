import pymysql
class Database():      
	def __init__(self,app):
		self.app = app

	def getconn(self):
		c = self.app.config
		db = pymysql.connect(c['DBHOST'],c['DBUSER'],c['DBPASS'],c['DBNAME'])
		return db 

  
	def get_single_val_query(self,str,params=[]):
		try:
			conn = self.getconn()
			cur = conn.cursor()
			try:
				cur.execute(str,params)
				result = cur.fetchone()
				# self.app.logger.debug(cur._last_executed)
				cur.close()
				return result
			finally:
				conn.close() 
		except Exception as e:
			self.app.logger.error(e,exc_info=True)
			raise RuntimeError('oops') from e

	def get_multi_val_query(self,str,params=[]):
		try:
			#self.app.logger.debug('multival query before exec: {}'.format(str))
			conn = self.getconn()
			cur = conn.cursor(pymysql.cursors.DictCursor)
			try:
				cur.execute(str,params)
				result = cur.fetchall()
				#self.app.logger.debug('multival query after exec: {}'.format(cur._last_executed))
				cur.close()
				return result
			finally:
				conn.close() 
		except Exception as e:
			self.app.logger.error(e,exc_info=True)
			raise RuntimeError('oops') from e
  
	def commit_sql(self, sql, params=[]):
		conn = self.getconn()
		cur = conn.cursor()
		try:
			cur.execute(sql, params)
			conn.commit()
		except Exception as e:
			conn.rollback()
			self.app.logger.error(e)
			raise RuntimeError(str(e))
		finally:
			conn.close()

	def constructSQL(self,select_fields,table_name,criterias=[],order_by=[],limit=0,offset=0,group_by_cols=[]):
		sql = 'SELECT ' + ",".join(select_fields) + ' FROM ' + table_name
		
		for i in range(0,len(criterias)):
			sql = self.__addCriteria(sql,criterias[i],i)

		if len(group_by_cols)>0:
			sql = sql +' GROUP BY ' + ",".join(group_by_cols)
		
		if len(order_by)>0:
			sql = sql +' ORDER BY ' + ",".join(order_by)
		
		if limit > 0:
			sql = sql +' LIMIT ' + str(limit)
		
		if offset > 0:
			sql = sql +' OFFSET ' + str(offset)
		
		return sql
	
	def constructSQLWithJoins(self,tables,join_criterias,order_by=[],limit=0,offset=0,group_by_cols=[]):
		sql = 'SELECT * ' + ' FROM ' + ",".join(tables)
		
		for i in range(0,len(join_criterias)):
			sql = self.__addCriteria(sql,join_criterias[i],i)

		if len(group_by_cols)>0:
			sql = sql +' GROUP BY ' + ",".join(group_by_cols)
		
		if len(order_by)>0:
			sql = sql +' ORDER BY ' + ",".join(order_by)
		
		if limit > 0:
			sql = sql +' LIMIT ' + str(limit)
		
		if offset > 0:
			sql = sql +' OFFSET ' + str(offset)
		
		return sql
	
	def __addCriteria(self,sql,criteria,idx):
		if idx == 0:
			criteria = ' WHERE '+criteria['str']
		else:
			criteria = ' '+criteria['type']+' '+criteria['str']
		sql = sql + criteria  
		return sql