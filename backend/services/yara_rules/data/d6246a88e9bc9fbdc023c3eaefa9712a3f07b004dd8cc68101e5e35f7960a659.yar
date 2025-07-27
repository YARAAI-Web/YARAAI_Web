rule auto_rule_20250726221445_0057 {
  strings:
    $o0 = "x140u" wide ascii nocase
    $o1 = "lpCharType" wide ascii nocase
    $o2 = "__freetlocinfo" wide ascii nocase
    $o3 = "TrailDown2" wide ascii nocase
    $o4 = "fccHandler" wide ascii nocase
  condition:
    5 of ($o*)
}