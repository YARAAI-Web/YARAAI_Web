rule auto_rule_20250726112656_8193 {
  strings:
    $o0 = "__sbh_heap_check" wide ascii nocase
    $o1 = "dwInfoType" wide ascii nocase
    $o2 = "_malloc_dbg" wide ascii nocase
    $o3 = "ReturnValue" wide ascii nocase
    $o4 = "GetStringTypeW" wide ascii nocase
  condition:
    5 of ($o*)
}