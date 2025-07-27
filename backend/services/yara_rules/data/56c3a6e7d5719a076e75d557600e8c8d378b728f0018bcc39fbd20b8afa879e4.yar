rule auto_rule_20250726211446_9960 {
  strings:
    $o0 = "fflush" wide ascii nocase
    $o1 = "_CrtMemDumpAllObjectsSince" wide ascii nocase
    $o2 = "_commit" wide ascii nocase
  condition:
    3 of ($o*)
}