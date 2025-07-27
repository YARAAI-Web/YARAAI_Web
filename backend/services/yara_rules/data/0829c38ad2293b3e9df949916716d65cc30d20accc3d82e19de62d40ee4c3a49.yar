rule auto_rule_20250726134010_4961 {
  strings:
    $o0 = "_output" wide ascii nocase
    $o1 = "IsBadWritePtr" wide ascii nocase
    $o2 = "off_469680" wide ascii nocase
    $o3 = "dword_469B90" wide ascii nocase
    $o4 = "_CrtMemDumpAllObjectsSince" wide ascii nocase
  condition:
    4 of ($o*)
}