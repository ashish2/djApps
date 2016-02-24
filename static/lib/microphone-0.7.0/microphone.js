/* microphone.js 0.7.0 */
(function() {
    var a, b, c, d, e, f;
    b = "0.7.0", navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia, window.AudioContext = window.AudioContext || window.webkitAudioContext || window.mozAudioContext || window.msAudioContext,
        function() {
            var a, b, c, d, e, f, g, h;
            for (e = window, h = ["ms", "moz", "webkit", "o"], f = 0, g = h.length; g > f && (d = h[f], !e.requestAnimationFrame); f++) e.requestAnimationFrame = e["" + d + "RequestAnimationFrame"], e.cancelAnimationFrame = e["" + d + "CancelAnimationFrame"] || e["" + d + "CancelRequestAnimationFrame"];
            if (e.requestAnimationFrame) {
                if (e.cancelAnimationFrame) return;
                return a = e.requestAnimationFrame, b = {}, e.requestAnimationFrame = function(c) {
                    var d;
                    return d = a(function(a) {
                        return d in b ? delete b[d] : c(a)
                    })
                }, e.cancelAnimationFrame = function(a) {
                    return b[a] = !0
                }
            }
            return c = 0, e.requestAnimationFrame = function(a) {
                var b;
                return c = Math.max(c + 16, b = +new Date), e.setTimeout(function() {
                    return a(+new Date)
                }, c - b)
            }, e.cancelAnimationFrame = function(a) {
                return clearTimeout(a)
            }
        }(), e = ("undefined" != typeof localStorage && null !== localStorage ? localStorage.getItem : void 0) && localStorage.getItem("wit_debug") ? function() {
            return console.log.apply(console, arguments)
        } : function() {}, d = function(a, b) {
            return this.name = "WitError", this.message = a || "", this.infos = b, this
        }, d.prototype = Error.prototype, c = "wss://api.wit.ai/speech_ws", a = function(a) {
            var b, c;
            return this.conn = null, this.ctx = new AudioContext, this.state = "disconnected", this.rec = !1, this.handleError = function(a) {
                var b, c;
                return _.isFunction(c = this.onerror) ? (b = _.isString(a) ? a : _.isString(a.message) ? a.message : "Something went wrong!", c.call(window, b, a)) : void 0
            }, this.handleResult = function(a) {
                var b, c, d;
                return _.isFunction(c = this.onresult) ? (d = a.outcome.intent, b = a.outcome.entities, c.call(window, d, b, a)) : void 0
            }, a && (this.elem = a, a.innerHTML = "<div class='mic mic-box icon-wit-mic'>\n</div>\n<svg class='mic-svg mic-box'>\n</svg>", a.className += " wit-microphone", a.addEventListener("click", function(a) {
                return function() {
                    return a.fsm("toggle_record")
                }
            }(this)), c = this.elem.children[1], b = "http://www.w3.org/2000/svg", this.path = document.createElementNS(b, "path"), this.path.setAttribute("stroke", "#eee"), this.path.setAttribute("stroke-width", "5"), this.path.setAttribute("fill", "none"), c.appendChild(this.path)), this.rmactive = function() {
                return this.elem ? this.elem.classList.remove("active") : void 0
            }, this.mkactive = function() {
                return this.elem ? this.elem.classList.add("active") : void 0
            }, this.mkthinking = function() {
                var a, b, d, e, f, g, h, i, j, k, l, m, n;
                return this.thinking = !0, this.elem ? (i = getComputedStyle(c), this.elem.classList.add("thinking"), l = parseInt(i.width, 10), f = parseInt(i.height, 10), b = "border-box" === i.boxSizing ? parseInt(i.borderTopWidth, 10) : 0, g = l / 2 - b - 5, a = 1e3, d = l / 2 - b, e = f / 2 - b - g, m = 0, j = 1, h = (null != (n = window.performance) ? n.now() : void 0) || new Date, k = function(c) {
                    return function(i) {
                        var n, o, p, q;
                        return o = (i - h) % a / a * 2 * Math.PI - Math.PI / 2, p = Math.cos(o) * g + l / 2 - b, q = Math.sin(o) * g + f / 2 - b, n = +(1.5 * Math.PI > o && o > Math.PI / 2), c.path.setAttribute("d", "M" + d + "," + e + "A" + g + "," + g + "," + m + "," + n + "," + j + "," + p + "," + q), c.thinking ? requestAnimationFrame(k) : (c.elem.classList.remove("thinking"), c.path.setAttribute("d", "M0,0"))
                    }
                }(this), requestAnimationFrame(k)) : void 0
            }, this.rmthinking = function() {
                return this.thinking = !1
            }, this
        }, f = {
            disconnected: {
                connect: function(a) {
                    var b, d;
                    return a || this.handleError("No token provided"), b = new WebSocket(c), b.onopen = function() {
                        return function(c) {
                            var d;
                            return e("connection opened", c), d = {
                                token: a,
                                bps: 16,
                                encoding: "signed-integer"
                            }, b.send(JSON.stringify(["auth", d]))
                        }
                    }(this), b.onclose = function(a) {
                        return function() {
                            return a.fsm("socket_closed")
                        }
                    }(this), b.onmessage = function(a) {
                        return function(b) {
                            var c, d, e;
                            return e = JSON.parse(b.data), d = e[0], c = e[1], c ? a.fsm.call(a, d, c) : a.fsm.call(a, d)
                        }
                    }(this), this.conn = b, d = function(a) {
                        return function(b) {
                            var c, d, f;
                            return c = a.ctx, f = c.createMediaStreamSource(b), d = (c.createScriptProcessor || c.createJavascriptNode).call(c, 4096, 1, 1), d.onaudioprocess = function(b) {
                                var c, d, f, g, h, i, j, k;
                                if (a.rec) {
                                    for (c = b.inputBuffer, d = c.getChannelData(0), h = d.length, g = new Int16Array(h), f = k = 0; h >= 0 ? h >= k : k >= h; f = h >= 0 ? ++k : --k) i = d[f], j = 0 > i ? 32768 * i : 32767 * i, g[f] = j;
                                    return e("[audiobuffer] rate=" + c.sampleRate + ", samples=" + h + ", bytes=" + g.byteLength), a.conn.send(g)
                                }
                            }, f.connect(d), d.connect(c.destination), a.stream = b, a.proc = d, a.src = f, a.fsm("got_stream")
                        }
                    }(this), navigator.getUserMedia({
                        audio: !0
                    }, d, this.handleError), "connecting"
                }
            },
            connecting: {
                "auth-ok": function() {
                    return "waiting_for_stream"
                },
                got_stream: function() {
                    return "waiting_for_auth"
                },
                error: function(a) {
                    return this.handleError(a), "connecting"
                },
                socket_closed: function() {
                    return "disconnected"
                }
            },
            waiting_for_auth: {
                "auth-ok": function() {
                    return "ready"
                }
            },
            waiting_for_stream: {
                got_stream: function() {
                    return "ready"
                }
            },
            ready: {
                socket_closed: function() {
                    return "disconnected"
                },
                timeout: function() {
                    return "ready"
                },
                start: function() {
                    return this.fsm("toggle_record")
                },
                toggle_record: function() {
                    return this.conn.send(JSON.stringify(["start", this.context || {}])), this.rec = !0, this.ctx || console.error("No context"), this.stream || console.error("No stream"), this.src || console.error("No source"), this.proc || console.error("No processor"), "audiostart"
                }
            },
            audiostart: {
                error: function(a) {
                    return this.rec = !1, this.handleError(new d("Error during recording", {
                        code: "RECORD",
                        data: a
                    })), "ready"
                },
                socket_closed: function() {
                    return this.rec = !1, "disconnected"
                },
                stop: function() {
                    return this.fsm("toggle_record")
                },
                toggle_record: function() {
                    return this.rec = !1, this.conn.send(JSON.stringify(["stop"])), this.timer = setTimeout(function(a) {
                        return function() {
                            return a.fsm("timeout")
                        }
                    }(this), 6e4), "audioend"
                }
            },
            audioend: {
                socket_closed: function() {
                    return this.timer && clearTimeout(this.timer), "disconnected"
                },
                timeout: function() {
                    return this.handleError(new d("Wit timed out", {
                        code: "TIMEOUT"
                    })), "ready"
                },
                error: function(a) {
                    return this.timer && clearTimeout(this.timer), this.handleError(new d("Wit did not recognize intent", {
                        code: "RESULT",
                        data: a
                    })), "ready"
                },
                result: function(a) {
                    return this.timer && clearTimeout(this.timer), this.handleResult(a), "ready"
                }
            }
        }, a.prototype.fsm = function(a) {
            var b, c, d, g;
            if (c = null != (g = f[this.state]) ? g[a] : void 0, b = Array.prototype.slice.call(arguments, 1), _.isFunction(c)) switch (d = c.apply(this, b), e("fsm: " + this.state + " + " + a + " -> " + d, b), this.state = d, ("audiostart" === d || "audioend" === d || "ready" === d || "connecting" === d || "disconnected" === d) && _.isFunction(c = this["on" + d]) && c.call(window), d) {
                case "disconnected":
                    this.rmthinking(), this.rmactive();
                    break;
                case "ready":
                    this.rmthinking(), this.rmactive();
                    break;
                case "audiostart":
                    this.mkactive();
                    break;
                case "audioend":
                    this.mkthinking(), this.rmactive()
            } else e("fsm error: " + this.state + " + " + a, b);
            return d
        }, a.prototype.connect = function(a) {
            return this.fsm("connect", a)
        }, a.prototype.start = function() {
            return this.fsm("start")
        }, a.prototype.stop = function() {
            return this.fsm("stop")
        }, a.prototype.setContext = function(a) {
            var b, c;
            this.context || (this.context = {});
            for (b in a) c = a[b], this.context[b] = a[b];
            return e("context: ", this.context), null
        }, window._ || (window._ = {}), _.isFunction || (_.isFunction = function(a) {
            return "function" == typeof a
        }), _.isString || (_.isString = function(a) {
            return "[object String]" === toString.call(a)
        }), window.Wit || (window.Wit = {}), Wit.Microphone = a
}).call(this);
