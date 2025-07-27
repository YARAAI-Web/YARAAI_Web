rule auto_rule_20250727024247_3961 {
  strings:
    $o0 = "__sbh_heap_check" wide ascii nocase
    $o1 = "_CrtMemDumpAllObjectsSince" wide ascii nocase
    $o2 = "UsedDefaultChar" wide ascii nocase
    $o3 = "lRequest" wide ascii nocase
  condition:
    4 of ($o*)
}