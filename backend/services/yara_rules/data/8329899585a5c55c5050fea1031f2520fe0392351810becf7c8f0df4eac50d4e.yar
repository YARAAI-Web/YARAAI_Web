rule auto_rule_20250726103128_5194 {
  strings:
    $o0 = "dword_4690AC" wide ascii nocase
    $o1 = "_heap_alloc_dbg" wide ascii nocase
    $o2 = "_CrtSetDbgFlag" wide ascii nocase
    $o3 = "__sbh_alloc_new_region" wide ascii nocase
    $o4 = "IsBadReadPtr" wide ascii nocase
  condition:
    4 of ($o*)
}