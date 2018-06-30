def bisect_find(array, x):
	
	m_min, m_max = 0, len(array)
		
	while m_min != m_max:
		
		mid = (m_min + m_max) // 2
		
		if nums1[mid] < x:
			m_min = mid + 1
		else:
			m_max = mid
		
	return m_min