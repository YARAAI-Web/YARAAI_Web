rule auto_rule_20250726151601_5345 {
  strings:
    $o0 = "located" wide ascii nocase
    $o1 = "TrailDown0" wide ascii nocase
    $o2 = "szUserMessage" wide ascii nocase
  condition:
    3 of ($o*)
}