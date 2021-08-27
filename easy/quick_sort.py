"""
simple sort , not very effective, only for learning and interview
"""

def qsort(ar):
  if not ar:
    return []
  return (
          qsort([i for i in ar[1:] if i < ar[0]])
          + [ar[0]] + 
          qsort([i for i in ar[1:] if i >= ar[0]])
          )
