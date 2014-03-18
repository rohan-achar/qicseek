# XBIF parser
# -----------
# Reads an XBIF file and converts it to the SIMPLE file format
# Author: Radu Marinescu <radum@ics.uci.edu>

import sys
from xml.dom import minidom


class XBifParser:

	variables = { }
	probabilities = { }
	observations = 0
	id2name = { }
	
	def name2id(self, var):
		return self.variables[var][0]
	
	def read(self, filename):
		print 'parsing "%s" file ...' % filename
		xmldoc = minidom.parse(filename)
		self.observations = 0
		
		# Variables
		for var in xmldoc.getElementsByTagName('VARIABLE'):
			v_name = ''
			v_size = 0
			v_observed = -1
			for child in var.childNodes:
				if (child.nodeName == u'NAME'):
					v_name = child.childNodes[0].nodeValue.encode('ascii')
				elif (child.nodeName == u'VALUES'):
					v_size = int(child.childNodes[0].nodeValue.encode('ascii'))
				elif (child.nodeName == u'OBSERVED'):
					v_observed = int(child.childNodes[0].nodeValue.encode('ascii'))
					self.observations = self.observations + 1
			id = len(self.variables)
			self.variables[v_name] = (id, v_size, v_observed)
			self.id2name[id] = v_name

		# Probabilities
		for cpt in xmldoc.getElementsByTagName('PROBABILITY'):
			scope = ()
			table = ()
			for child in cpt.childNodes:
				if (child.nodeName == u'FOR'):
					ch = child.childNodes[0].nodeValue.encode('ascii')
					scope += (ch,)
				elif (child.nodeName == u'GIVEN'):
					par = child.childNodes[0].nodeValue.encode('ascii')
					scope += (par,)
				elif (child.nodeName == u'TABLE'):
					table = child.childNodes[0].nodeValue.encode('ascii')
			self.probabilities[scope[0]] = (scope, table)
			
		# Print data
##		for v0,v1 in self.variables.iteritems():
##			print v0,v1
##		for p0,p1 in self.probabilities.iteritems():
##			print p0,p1

	def write(self, filename):
		try:
			f = open(filename, 'w')
			print 'writing "%s" file ...' % filename
			
			# Header
			f.write('network Unknown\n')
			f.write('f lsb\n')
			if not self.observations: f.write('e no 0\n')
			else: f.write('e yes %d\n' % self.observations)
			f.write('%d\n' % len(self.variables))

			# Variables
			var_keys = self.id2name.keys()
			var_keys.sort()
			for id in var_keys:
				name = self.id2name[id]
				content = self.variables[name]
				cpt = self.probabilities[name]
				parents = len(cpt[0])-1
				if not self.observations:
					f.write('v %d %d %d %s\n' %(content[0],content[1],parents,name))
				else:
					f.write('v %d %d %d %d %s\n' % (content[0],content[1],content[2],parents,name))

			# Probabilities
			for id in var_keys:
				name = self.id2name[id]
				cpt = self.probabilities[name]
				scope = cpt[0]
				f.write('p ')
				for p in scope[1:]: f.write('%d ' % self.name2id(p))
				f.write('%d\n' % self.name2id(scope[0]))
				table = cpt[1]
				for chunk in table.split("\n"):
					if (len(chunk) > 0): f.write('%s ' % chunk.strip(" \t"))
				f.write('\n')

			f.close()
			print 'done.'
			
		except:
			f.close()
			print 'error'
			raise

xbif = XBifParser()
infilename = sys.argv[1]
xbif.read(infilename)

outfilename = infilename.rstrip("xbif") + "simple"
xbif.write(outfilename)


