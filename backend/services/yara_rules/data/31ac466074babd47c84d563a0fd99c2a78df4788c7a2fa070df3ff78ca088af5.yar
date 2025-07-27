rule auto_rule_20250726131134_2396 {
  strings:
    $o0 = "lpPathSpec" wide ascii nocase
    $o1 = "redraw" wide ascii nocase
    $o2 = "IMPQueryIMEW" wide ascii nocase
  condition:
    3 of ($o*)
}