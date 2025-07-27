rule auto_rule_20250727032947_5296 {
  strings:
    $o0 = "Debug" wide ascii nocase
    $o1 = "_CrtMemDumpAllObjectsSince" wide ascii nocase
    $o2 = "subtype" wide ascii nocase
    $o3 = "Offset" wide ascii nocase
    $o4 = "x41C4u" wide ascii nocase
  condition:
    5 of ($o*)
}