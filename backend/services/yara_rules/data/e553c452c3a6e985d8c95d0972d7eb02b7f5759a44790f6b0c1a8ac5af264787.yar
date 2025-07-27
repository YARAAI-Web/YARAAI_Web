rule auto_rule_20250726182310_8363 {
  strings:
    $o0 = "_pLastBlock" wide ascii nocase
    $o1 = "_heapchk" wide ascii nocase
    $o2 = "dword_4693F8" wide ascii nocase
    $o3 = "UnwindUp2_0" wide ascii nocase
    $o4 = "TrailDown1_0" wide ascii nocase
  condition:
    4 of ($o*)
}