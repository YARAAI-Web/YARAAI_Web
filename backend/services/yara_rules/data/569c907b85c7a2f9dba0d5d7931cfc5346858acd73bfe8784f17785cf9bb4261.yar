rule auto_rule_20250726195404_6243 {
  strings:
    $o0 = "stream" wide ascii nocase
    $o1 = "_nh_malloc_dbg" wide ascii nocase
    $o2 = "dword_469CE4" wide ascii nocase
    $o3 = "asserts" wide ascii nocase
    $o4 = "fails" wide ascii nocase
  condition:
    4 of ($o*)
}