rule auto_rule_20250726103659_0939 {
  strings:
    $o0 = "_heapchk" wide ascii nocase
    $o1 = "_heap_alloc_dbg" wide ascii nocase
  condition:
    all of them
}