rule auto_rule_20250727044148_3829 {
  strings:
    $o0 = "__sbh_alloc_block" wide ascii nocase
    $o1 = "dword_462020" wide ascii nocase
    $o2 = "dbgrpt" wide ascii nocase
    $o3 = "_CrtMemDumpAllObjectsSince" wide ascii nocase
    $o4 = "_cinit" wide ascii nocase
  condition:
    4 of ($o*)
}